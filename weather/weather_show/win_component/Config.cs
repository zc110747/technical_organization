using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace win_component
{
    class Config
    {    
        public string MqttSever = "192.168.16.52";

        public int MqttPort = 1883;

        public string MqttSubscribeTopic = "/public/weather/1";
        
        public string MqttPublishTopic = "/public/weather/2";

        public string MqttClientID = "c#_client";

        public string LoggerIpAddr = "192.168.16.52";

        public int LoggerPort = 15059;

        public bool LoadSystemConfig(string file)
        {
            try
            {
                if (File.Exists(file))
                {
                    string FileStr = File.ReadAllText(file);
                    JObject jarr = JObject.Parse(FileStr);


                    LoggerIpAddr = ((jarr["socket"])!["socket_ip"]!).ToString();
                    LoggerPort = int.Parse(((jarr["socket"])!["logger_port"]!).ToString());

                    MqttSubscribeTopic = (jarr["res_topic"])!.ToString();
                    MqttPublishTopic = (jarr["req_topic"])!.ToString();

                    bool use_remote = (jarr["use_remote"])!.ToString().Equals("True");
                    if (use_remote)
                    {
                        MqttSever = ((jarr["remote_mqtt"])!["socket_ip"]!).ToString();
                        MqttPort = int.Parse(((jarr["remote_mqtt"])!["port"]!).ToString());
                    }
                    else
                    {
                        MqttSever = ((jarr["local_mqtt"])!["socket_ip"]!).ToString();
                        MqttPort = int.Parse(((jarr["local_mqtt"])!["port"]!).ToString());
                    }
                }
                else
                {
                    return false;
                }

                return true;
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }
    }
}
