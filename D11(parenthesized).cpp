#include <iostream> 
using namespace std; 
#define size 10

class stackexp
{
int top;
char stk[size];

public:
stackexp()
{
top=-1;
}

void push(char); char pop();
int isfull(); int isempty();
};

void stackexp::push(char x)
{
top=top+1; //increment top stk[top]=x;
}



char stackexp::pop()
{
char s; 
s=stk[top];
top=top-1;//decrement the top return s;
return s;
}


int stackexp::isfull() //to check stack is full
{

if(top==size) return 1;
else return 0;
}

int stackexp::isempty()//to check stack is
{
if(top==-1) return 1; else
return 0;
}

int main()
{
stackexp s1; //its object of class
char exp[20],ch;
int i=0;

cout<<"****************PRACTICAL NO-11(D-26)*****************"; cout<<"\nenter the expression to check whether it is in well form or not : "; cin>>exp;

if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))
{
cout<<"\n Invalid Expression.	\n";
return 0;
}

else
{
while(exp[i]!='\0')
{
ch=exp[i];

switch(ch)
{
case '(':s1.push(ch);break;
case '[':s1.push(ch);break;
case '{':s1.push(ch);break;
case ')':s1.pop();break;
case ']':s1.pop();break;
case '}':s1.pop();break;
}
i=i+1; //5
}
}
if(s1.isempty())

{
cout<<"\nExpression is well parenthesis...\n";
}

else
{
cout<<"\nSorry !!! Invalid Expression or not in well parenthesized.	\n";
}
return 0;
}
