namespace win_component
{
    partial class win_component
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(win_component));
            this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
            this.TimerLabel = new System.Windows.Forms.Label();
            this.CpuTempLabel = new System.Windows.Forms.Label();
            this.ReceiveCntLabel = new System.Windows.Forms.Label();
            this.RamFreeLabel = new System.Windows.Forms.Label();
            this.DiskFreeLabel = new System.Windows.Forms.Label();
            this.weather = new System.Windows.Forms.Label();
            this.tempature = new System.Windows.Forms.Label();
            this.CpuUsageLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // notifyIcon1
            // 
            this.notifyIcon1.Text = "notifyIcon1";
            this.notifyIcon1.Visible = true;
            // 
            // TimerLabel
            // 
            this.TimerLabel.AutoSize = true;
            this.TimerLabel.BackColor = System.Drawing.Color.Transparent;
            this.TimerLabel.Font = new System.Drawing.Font("宋体", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.TimerLabel.ForeColor = System.Drawing.Color.DeepPink;
            this.TimerLabel.Location = new System.Drawing.Point(15, 225);
            this.TimerLabel.Name = "TimerLabel";
            this.TimerLabel.Size = new System.Drawing.Size(238, 24);
            this.TimerLabel.TabIndex = 0;
            this.TimerLabel.Text = "2023-10-13 23:15:12";
            // 
            // CpuTempLabel
            // 
            this.CpuTempLabel.BackColor = System.Drawing.Color.Transparent;
            this.CpuTempLabel.Font = new System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.CpuTempLabel.ForeColor = System.Drawing.Color.OrangeRed;
            this.CpuTempLabel.Location = new System.Drawing.Point(280, 225);
            this.CpuTempLabel.Name = "CpuTempLabel";
            this.CpuTempLabel.Size = new System.Drawing.Size(182, 24);
            this.CpuTempLabel.TabIndex = 2;
            this.CpuTempLabel.Text = "CPU Tempature:0.0°";
            // 
            // ReceiveCntLabel
            // 
            this.ReceiveCntLabel.BackColor = System.Drawing.Color.Transparent;
            this.ReceiveCntLabel.Font = new System.Drawing.Font("Courier New", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.ReceiveCntLabel.ForeColor = System.Drawing.Color.OrangeRed;
            this.ReceiveCntLabel.Location = new System.Drawing.Point(364, 249);
            this.ReceiveCntLabel.Name = "ReceiveCntLabel";
            this.ReceiveCntLabel.Size = new System.Drawing.Size(90, 23);
            this.ReceiveCntLabel.TabIndex = 3;
            this.ReceiveCntLabel.Text = "count:0000";
            // 
            // RamFreeLabel
            // 
            this.RamFreeLabel.AutoSize = true;
            this.RamFreeLabel.BackColor = System.Drawing.Color.Transparent;
            this.RamFreeLabel.Font = new System.Drawing.Font("Courier New", 10.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.RamFreeLabel.ForeColor = System.Drawing.Color.OrangeRed;
            this.RamFreeLabel.Location = new System.Drawing.Point(280, 165);
            this.RamFreeLabel.Name = "RamFreeLabel";
            this.RamFreeLabel.Size = new System.Drawing.Size(174, 20);
            this.RamFreeLabel.TabIndex = 4;
            this.RamFreeLabel.Text = "RAM Free:0000MB";
            // 
            // DiskFreeLabel
            // 
            this.DiskFreeLabel.AutoSize = true;
            this.DiskFreeLabel.BackColor = System.Drawing.Color.Transparent;
            this.DiskFreeLabel.Font = new System.Drawing.Font("Courier New", 10.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.DiskFreeLabel.ForeColor = System.Drawing.Color.OrangeRed;
            this.DiskFreeLabel.Location = new System.Drawing.Point(280, 92);
            this.DiskFreeLabel.Name = "DiskFreeLabel";
            this.DiskFreeLabel.Size = new System.Drawing.Size(174, 20);
            this.DiskFreeLabel.TabIndex = 5;
            this.DiskFreeLabel.Text = "Disk Free:000GB";
            // 
            // weather
            // 
            this.weather.AutoSize = true;
            this.weather.BackColor = System.Drawing.Color.Transparent;
            this.weather.Font = new System.Drawing.Font("Microsoft YaHei UI", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.weather.ForeColor = System.Drawing.Color.DeepPink;
            this.weather.Location = new System.Drawing.Point(33, 33);
            this.weather.Name = "weather";
            this.weather.Size = new System.Drawing.Size(124, 104);
            this.weather.TabIndex = 6;
            this.weather.Text = "晴";
            // 
            // tempature
            // 
            this.tempature.AutoSize = true;
            this.tempature.BackColor = System.Drawing.Color.Transparent;
            this.tempature.Font = new System.Drawing.Font("Microsoft YaHei UI", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.tempature.ForeColor = System.Drawing.Color.DeepPink;
            this.tempature.Location = new System.Drawing.Point(54, 137);
            this.tempature.Name = "tempature";
            this.tempature.Size = new System.Drawing.Size(72, 31);
            this.tempature.TabIndex = 7;
            this.tempature.Text = "00.0°";
            // 
            // CpuUsageLabel
            // 
            this.CpuUsageLabel.AutoSize = true;
            this.CpuUsageLabel.BackColor = System.Drawing.Color.Transparent;
            this.CpuUsageLabel.Font = new System.Drawing.Font("Courier New", 10.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.CpuUsageLabel.ForeColor = System.Drawing.Color.OrangeRed;
            this.CpuUsageLabel.Location = new System.Drawing.Point(280, 195);
            this.CpuUsageLabel.Name = "CpuUsageLabel";
            this.CpuUsageLabel.Size = new System.Drawing.Size(141, 20);
            this.CpuUsageLabel.TabIndex = 8;
            this.CpuUsageLabel.Text = "CPU Usage:0%";
            // 
            // win_component
            // 
            this.BackColor = System.Drawing.Color.WhiteSmoke;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.ClientSize = new System.Drawing.Size(462, 273);
            this.Controls.Add(this.CpuUsageLabel);
            this.Controls.Add(this.tempature);
            this.Controls.Add(this.weather);
            this.Controls.Add(this.DiskFreeLabel);
            this.Controls.Add(this.RamFreeLabel);
            this.Controls.Add(this.ReceiveCntLabel);
            this.Controls.Add(this.CpuTempLabel);
            this.Controls.Add(this.TimerLabel);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(480, 320);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(480, 320);
            this.Name = "win_component";
            this.Text = "WinComponent";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private NotifyIcon notifyIcon1;
        private Label TimerLabel;
        private Label CpuTempLabel;
        private Label ReceiveCntLabel;
        private Label RamFreeLabel;
        private Label DiskFreeLabel;
        private Label weather;
        private Label tempature;
        private Label CpuUsageLabel;
    }
}