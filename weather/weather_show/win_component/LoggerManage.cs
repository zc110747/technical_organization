using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Timers;

/*
 * 用于打印调试信息的logger客户端
 * 在调用前需要开启TCP服务器(使用TCP调试工具即可)
 * WriteString(string text)，可将信息打印到远端服务器
 * 可替代UI环境下Console.WriteLine打印不
 * 支持重连机制,需要调用logger打印接口, 才可以触发重连动作
 */
namespace win_component
{
    internal class LoggerManage
    {
        static private Socket? TcpSocket = null;
        static private bool is_tcp_connect = false;
        static private System.Timers.Timer? _timer = null;
        static private string LocalIpAddr = "127.0.0.1";
        static private int LocalPort = 0;
        static private bool is_timer_on = false;

        static private void TimerDetectHandler(object? sender, ElapsedEventArgs e)
        {
            if(!is_tcp_connect
              || TcpSocket == null
              || !TcpSocket.Connected)
            {
                is_tcp_connect = TcpSocketConnet();
                if (is_tcp_connect)
                {
                    WriteString("Detect Sever Ok, Connect Success!");
                }
            }
            else
            {
                //do nothing
            }
        }

        static private void StartDetectTimer(double time)
        {
            if(!is_timer_on)
            {
                _timer = new System.Timers.Timer(time);
                _timer.AutoReset = true;
                _timer.Elapsed += TimerDetectHandler;
                _timer.Start();
    
                is_timer_on = true;
            }
        }

        static private void StopDetectTimer()
        {
            if(_timer != null)
            {
                _timer.Stop();
                _timer.Dispose();
            }
            is_timer_on = false;

        }

        static private bool TcpSocketConnet()
        {
            try
            {
                IPEndPoint IpGlobal = new IPEndPoint(IPAddress.Parse(LocalIpAddr), LocalPort);
                TcpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                TcpSocket.ExclusiveAddressUse = false;
                TcpSocket.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
                TcpSocket.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.KeepAlive, true);
                TcpSocket.Connect(IpGlobal);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
                return false;
            }
        }

        static public bool logger_init(string ipAddress, int port)
        {
            LocalIpAddr = ipAddress;
            LocalPort = port;

            is_tcp_connect = TcpSocketConnet();
            StartDetectTimer(5000);
            return is_tcp_connect;
        }

        static public int WriteString(string text)
        {
            try
            {
                if (TcpSocket == null || is_tcp_connect == false)
                {
                    return 0;
                }

                if (!TcpSocket.Connected)
                {
                    return 0;
                }

                text += "\r\n";
                byte[] sendBytes = new byte[text.Length];
                sendBytes = Encoding.UTF8.GetBytes(text);
                TcpSocket.Send(sendBytes, sendBytes.Length, 0);
                return sendBytes.Length;
            }
            catch(Exception ex)
            {
                is_tcp_connect = false;
                Console.WriteLine(ex.Message);
                return 0;
            }
        }

    }
}
