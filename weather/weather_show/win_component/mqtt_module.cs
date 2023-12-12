using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using MQTTnet;
using MQTTnet.Client;
using MQTTnet.Server;

namespace win_component
{
    class mqtt_module
    {
        private IMqttClient? mqttClient = null;
        private bool mqttEnable = false;

        public bool getState()
        { 
            return mqttEnable; 
        }

        public async void mqtt_task_init(Config Config, Func<MqttApplicationMessageReceivedEventArgs, Task> handler)
        {
            try
            {
                mqttClient = new MqttFactory().CreateMqttClient();

                var options = new MqttClientOptionsBuilder()
                .WithTcpServer(Config.MqttSever, Config.MqttPort)
                .WithClientId(Config.MqttClientID)
                .WithCleanSession()
                .Build();

                await mqttClient.ConnectAsync(options);

                await mqttClient.SubscribeAsync(new MqttTopicFilterBuilder()
                .WithTopic(Config.MqttSubscribeTopic)
                .WithQualityOfServiceLevel(MQTTnet.Protocol.MqttQualityOfServiceLevel.AtLeastOnce)
                .Build());

                mqttClient.ApplicationMessageReceivedAsync += handler;

                mqttEnable = true;
            }
            catch(Exception ex)
            {
                mqttEnable = false;
                LoggerManage.WriteString(ex.ToString());
            }
        }
    }
}
