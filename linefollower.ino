int speed=120;
void setup() {pinMode(5,OUTPUT);//left live
pinMode(6,OUTPUT);//left grnd
pinMode(10,OUTPUT);//right live
pinMode(11,OUTPUT);//right grnd
 
}

void loop() {int a1=digitalRead(4);
int a2=digitalRead(7);
int a3=digitalRead(8);
int a4=digitalRead(9);
int a5=digitalRead(12);
int a6=digitalRead(13);
if((a1==1&&a2==1&&a3==0&&a4==0&&a5==1&&a6==1)||//forward
    (a1==1&&a2==1&&a3==1&&a4==0&&a5==1&&a6==1)||
    (a1==1&&a2==1&&a3==0&&a4==1&&a5==1&&a6==1))
    {analogWrite(5,speed);
    analogWrite(6,0);
    analogWrite(10,speed);
    analogWrite(11,0);
    }
else if((a1==1&&a2==0&&a3==0&&a4==1&&a5==1&&a6==1)||//left turn
        (a1==1&&a2==0&&a3==0&&a4==0&&a5==1&&a6==1)||
        (a1==1&&a2==0&&a3==1&&a4==1&&a5==1&&a6==1))
        {
          analogWrite(5,0);
          analogWrite(6,0);
          analogWrite(10,speed);
          analogWrite(11,0);
        }
        else if((a1==0&&a2==0&&a3==1&&a4==1&&a5==1&&a6==1)||//sharp left
                 (a1==0&&a2==0&&a3==0&&a4==1&&a5==1&&a6==1)||
                 (a1==0&&a2==0&&a3==0&&a4==0&&a5==1&&a6==1)||
                 (a1==0&&a2==0&&a3==0&&a4==0&&a5==0&&a6==1)||
                 (a1==0&&a2==0&&a3==0&&a4==0&&a5==0&&a6==0)||
                 (a1==0&&a2==1&&a3==0&&a4==0&&a5==1&&a6==1))
                 {
                  analogWrite(5,0);
                  analogWrite(6,speed);
                  analogWrite(10,speed);
                  analogWrite(11,0);
                 
                 }

else if((a1==1&&a2==1&&a3==0&&a4==0&&a5==0&&a6==1)||//right turn
         (a1==1&&a2==1&&a3==1&&a4==0&&a5==0&&a6==1)||
         (a1==1&&a2==1&&a3==1&&a4==1&&a5==0&&a6==1))
         {
          analogWrite(5,speed);
          analogWrite(6,0);
          analogWrite(10,0);
          analogWrite(11,0);
         }
         else if((a1==1&&a2==1&&a3==1&&a4==1&&a5==0&&a6==0)||//sharp right
                 (a1==1&&a2==1&&a3==1&&a4==0&&a5==0&&a6==0)||
                 (a1==1&&a2==1&&a3==0&&a4==0&&a5==0&&a6==0)||
                 (a1==1&&a2==0&&a3==0&&a4==0&&a5==0&&a6==0)||
                 (a1==1&&a2==1&&a3==0&&a4==0&&a5==1&&a6==0))
                 {
                  analogWrite(5,speed);
                  analogWrite(6,0);
                  analogWrite(10,0);
                  analogWrite(11,speed);
                 }
                 else
                 {
                  analogWrite(5,speed);
                  analogWrite(6,0);
                  analogWrite(10,speed);
                  analogWrite(11,0);
                 }
         
  

}
