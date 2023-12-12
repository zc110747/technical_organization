using MQTTnet;
using MQTTnet.Client;
using MQTTnet.Server;
using Newtonsoft.Json.Linq;
using System.Threading;
using System.Timers;

namespace win_component
{
    public partial class win_component : Form
    {
        private mqtt_module? g_mqtt = null;
        private Config? g_config = null;
        private readonly string ConfigFile = "config.json";
        private UInt32 mq_rx_cnt = 0;
        private System.Timers.Timer? _timer = null;
        private DateTime lastTime = DateTime.MinValue;

        //跨线程更新GUI的方案可以使用全局或者单个标签的委托
        //下面分别为两种不同的方式
        private delegate void AppendMethod(string str);
        private AppendMethod? TimeLabelString;
        static private SynchronizationContext? synchronizationContext = null;

        //绘圆的格式
        private float ram_percentage = 0;
        private float disk_percentage = 0;
        private float cpu_percentage = 0;
        public win_component()
        {
            InitializeComponent();

            synchronizationContext = SynchronizationContext.Current;

            this.Load += MyWindow_Loaded;
        }

        private void MyWindow_Loaded(object? sender, EventArgs e)
        {
            g_mqtt = new mqtt_module();
            g_config = new Config();
            TimeLabelString = new AppendMethod(str =>
            {
                this.TimerLabel.Text = str;
            });

            if (g_config.LoadSystemConfig(ConfigFile))
            {
                if (LoggerManage.logger_init(g_config.LoggerIpAddr, g_config.LoggerPort))
                {
                    LoggerManage.WriteString($"logger client start, ip:{g_config.LoggerIpAddr}, port:${g_config.LoggerPort}");
                }
                g_mqtt.mqtt_task_init(g_config, mqtt_sync_ui);
                if (g_mqtt.getState())
                {
                    LoggerManage.WriteString($"mqtt Subscribe success, server:{g_config.MqttSever}, port:${g_config.MqttSever}, topic:${g_config.MqttSubscribeTopic}");
                }
            }

            StartLoopTimer(100);
        }

        private void TimerLoopHandler(object? sender, ElapsedEventArgs e)
        {
            DateTime nowTime = DateTime.Now;
            if (lastTime.Second != nowTime.Second)
            {
                string timer_str = $"{nowTime.Year.ToString().PadLeft(4, '0')}-" +
                                $"{nowTime.Month.ToString().PadLeft(2, '0')}-" +
                                $"{nowTime.Day.ToString().PadLeft(2, '0')} " +
                                $"{nowTime.Hour.ToString().PadLeft(2, '0')}:" +
                                $"{nowTime.Minute.ToString().PadLeft(2, '0')}:" +
                                $"{nowTime.Second.ToString().PadLeft(2, '0')}";

                this.TimerLabel.Invoke(TimeLabelString, timer_str);
                lastTime = nowTime;
            }
        }

        private void StartLoopTimer(double time)
        {
            _timer = new System.Timers.Timer(time);
            _timer.AutoReset = true;
            _timer.Elapsed += TimerLoopHandler;
            _timer.Start();
        }

        /*
         {  "os": {"cpu_time": "2023-10-13, 10:45:27", "CPU_usage": "2.6", "CPU_temp": 0, 
                    "Disk_total": "223", "RAM_total": "16579", "RAM_used": "9702", "Disk_used": "112"}, 
            "weather": {"text": "\u6674", "temp": "21", "icon": "100"}
         }
         */
        private void UICallbackProcess(object? text)
        {
            if (text != null)
            {
                try
                {
                    //update rx cnt
                    mq_rx_cnt++;
                    if (mq_rx_cnt > 9999)
                        mq_rx_cnt = 0;
                    string mq_cnt_str = mq_rx_cnt.ToString().PadLeft(4, '0');
                    this.ReceiveCntLabel.Text = $"count:{mq_cnt_str}";

                    JObject jarr = JObject.Parse((string)text);

                    //温度
                    string tempature = ((jarr["os"])!["CPU_temp"])!.ToString();

                    //ram info
                    int ram_total = int.Parse(((jarr["os"])!["RAM_total"])!.ToString());
                    int ram_used = int.Parse(((jarr["os"])!["RAM_used"])!.ToString());
                    int ram_free = ram_total - ram_used;
                    ram_percentage = (float)ram_used / ram_total;

                    float disk_total = float.Parse(((jarr["os"])!["Disk_total"])!.ToString());
                    float disk_used = float.Parse(((jarr["os"])!["Disk_used"])!.ToString());
                    float disk_free = disk_total - disk_used;
                    disk_percentage = (float)disk_used / disk_total;

                    string weather = ((jarr["weather"])!["text"])!.ToString();
                    int weather_temp = int.Parse(((jarr["weather"])!["temp"])!.ToString());

                    float cpu_usage = float.Parse(((jarr["os"])!["CPU_usage"])!.ToString());
                    cpu_percentage = cpu_usage / 100;

                    this.CpuUsageLabel.Text = $"CPU Usage:{cpu_usage}%";
                    this.tempature.Text = $"{weather_temp}°";
                    this.weather.Text = weather;
                    this.RamFreeLabel.Text = $"RAM Free:{ram_free}MB";
                    this.DiskFreeLabel.Text = $"Disk Free:{disk_free}GB";
                    this.CpuTempLabel.Text = $"CPU Tempature:{tempature}°";
                    this.ReceiveCntLabel.Text = $"Count:{mq_rx_cnt}";
                    this.Invalidate();
                    LoggerManage.WriteString((string)text);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }
            }
        }

        public Task mqtt_sync_ui(MqttApplicationMessageReceivedEventArgs e)
        {
            synchronizationContext?.Post(UICallbackProcess, e.ApplicationMessage.ConvertPayloadToString());
            return Task.FromResult(true);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            Graphics g = e.Graphics;

            PainCircular(g, 320, 35, ram_percentage);

            PainCircular(g, 320, 115, disk_percentage);

            //PainCircular(g, 300, 20, cpu_percentage, 40, 30);
        }

        void PainCircular(Graphics g, UInt16 position_x, UInt16 position_y, float percent, int radio_e = 25, int radio_i = 15)
        {
            Rectangle rect_extend = new Rectangle(position_x, position_y, 2 * radio_e, 2 * radio_e);
            g.FillPie(Brushes.Azure, rect_extend, 0, 360);

            Rectangle rect_internal = new Rectangle(position_x + 10, position_y + 10, 2 * radio_i, 2 * radio_i);
            var angle = percent * 360;

            g.FillPie(Brushes.DarkOrange, rect_extend, 0, angle);
            g.DrawEllipse(Pens.Black, rect_extend);
        }
    }
}