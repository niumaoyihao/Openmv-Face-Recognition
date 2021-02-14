# Openmv-Face-Recognition
Face recognition based on openmv
# 思路
+ 主从关系：arduino主机，openmv从机
+ 继电器控制openmv的通断电
+ 为了省电，需要人脸识别的时候自己按按钮启动摄像头，摄像头将处理结果告诉arduino，后者控制舵机的运动体现门的开闭，加入门快速倒开推开人的骚操作
+ 识别到自己的人脸就门往里开，所以舵机需要转动角度大于180度
# 备注
+ 舵机需要外部供电，注意参考地要相同，否则会出现电流声并且乱转
+ openmv cam4，通讯为UART通讯，需要准备minisd卡。
+ arduino为UNO板
+ arduino使用I2C与LCD通讯，信号教关系为SCL->A5,SDA->A4
+ 舵机棕色线为GND，红线为VCC，橙线为信号，接9号PWM口
+ 外接可调电源需要电表校准到4.5V~5V之间，注意电线的裸露，避免碰短路
+ 使用的是270度舵机，从效果看，其角度并非绝对角度，有一点点误差
+ 启动按钮接R1C1，到VCC和2号pin，上拉输入
+ 继电器接5V，信号接4号pin 
