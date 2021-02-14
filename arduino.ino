#include<Wire.h>
#include<LiquidCrystal_I2C.h>
#include<string.h>
#include<Servo.h>



#define bottom 2//开始按键
#define relay 4//继电器控制口
Servo my_servo;  //创建一个舵机对象
LiquidCrystal_I2C lcd(0x27,16,2);//LCD写地址

String str="";//接收传输来的字符串
String str1="";//垃圾桶
String str2 = "close\0";
String str3="open\0";

void Change_my_servo(int angle,int delay_time)  //该算法可以控制舵机的运转速度
{
  for(int i=my_servo.read();i != angle; )
  {
    if(i > angle) i--;
    else i++;
    my_servo.write(i);
    delay(delay_time);
  } 
}
void my_servoInit()  //舵机初始化
{
  my_servo.attach(9);//9号PWM脚控制舵机
  my_servo.write(90);//默认90度关门
}


void setup()
{
  lcd.init();//LCD初始化
  lcd.backlight();
  Serial.begin(9600); //串口初始化，9600
  pinMode(bottom,INPUT);//开始按键初始化
  pinMode(relay,OUTPUT);//继电器控制口初始化
  digitalWrite(relay,LOW);
  my_servoInit();//舵机初始化
}

void loop()
{
  str = "";
  if(digitalRead(bottom)==HIGH)
  {
    delay(50);//消抖
    if(digitalRead(bottom)==HIGH)
    {
      digitalWrite(relay,HIGH);//继电器通电
      str1 = char(Serial.read());//垃圾桶收一个奇怪的字符
      
      while ((Serial.available()-1) > 0)
      {
        str += char(Serial.read());   // read是剪切，而不是复制
        delay(10);  // 延时
       
      }
      if (str.length() > 0)
      {
        
        //Serial.print(F("命令行发送内容："));
        //Serial.println(str);
       if(str.equals(str3))
        {
          Change_my_servo(0,10);//逆时针开门
          delay(3000);
          Change_my_servo(90,3);//关好
          digitalWrite(relay,LOW);
        }//判断是open就开门和断电
        if(str.equals(str2))
        {
          Change_my_servo(180,5);//顺时针踢人
          delay(30);
          Change_my_servo(90,3);//关好
          digitalWrite(relay,LOW);
        }//判断是close就踢人和断电
        lcd.setCursor(0,0);
        lcd.print(str);
      }
    }
  }
  delay(100);
  
}
