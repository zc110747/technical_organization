# win_component组件的实现
整个win_component组件的设计由三部分组成。<br />
1. 基于DoNetty.Codecs.Mqtt实现的mqtt订阅客户端
2. 基于Winform框架的UI界面构建
3. 数据更新UI同步到UI界面的回调(有变化才更新)
