### Equivalent to \`asctime (localtime(timer))\`  of time.h  
	time_t biggest= 0x7FFFFFFF;
        // ctime(&biggest) Equivalent asctime(localtime(&biggest))
        printf("%s",ctime(&biggest));
	
### 小技巧
	if(i==3) or if(3==i)
### 每个实参都应该具有自己的类型，这样它的值就可以赋值给与它所对应的形参类型的对象(该对象不能含有限定符)
	int foo(const char **p){}
	int main(int argc, char **argv)
	{
        	foo(argv);
	}
	
test.c:4:13: 警告：传递‘foo’的第 1 个参数时在不兼容的指针类型间转换 [-Wincompatible-pointer-types]
    4 |         foo(argv);
      |             ^~~~
      |             |
      |             char **
test.c:1:22: 附注：需要类型‘const char **’，但实参的类型为‘char **’
    1 | int foo(const char **p){}

update  

	int foo(const char **p){}
	int main(int argc,const char **argv)
	{
        	foo(argv);
	}

### 函数原型后面要加分号
	char * strcpy(char *dst,const char *src);
函数原型可以使编译时对函数调用实参和函数声明中的形参进行一致性检查

### NUL and NULL区别
	NUL用于结束一个ACSII字符串
	NULL表示空指针

### 相邻的字符串常量将被自动合并成一个字符串，在写多行信息时不必在行末加"\\"，但引入了新问题
	char *available_resouces[] = {
		"color monitor",
		"big disk"
		"Cray disk",
		}
字符串数目比预期少一个，引用会出错误，最后一个逗号存在或不存在都没有意义

### extern and static
定义C 函数时,缺省情况下函数名字全局可见,推荐冗余加上extern关键字，这样的话对于链接到它所在目标文件的任何东西都是可见的，如果想限制这个函数，必须加static关键字  
	function apple() { /* 在任何地方均可见 */}  
	extern function pear() { /* 在任何地方均可见 */}  
	static function turnip() { /* 在这个文件之外不可见 */}  

###  C语言符号重载
|符号|意义|
|:---:|:---:|
|static| 在函数内部表示该变量值在各个调用间保持延续性(程序运行期间局部变量不会随着函数销毁后再次调用而恢复初始值)  </br>
在函数这一级表示该函数只对本文件可见|
|extern| 用于函数定义，表示全局可见(函数默认使用extern)
用于变量，表示它在其他地方定义|
|void| 作为函数返回类型，表示不返回任何值
在指针声明中表示通用指针的类型
位于参数列表中表示没有参数|
|\*| 乘法运算符
用于指针，间接引用
在声明中，表示指针|
|&| 位的AND操作符
取地址符|
|<<=| 左移复合赋值运算符|
|<| 小于运算符
\#include 指令的左定界符|
|()| 在函数定义中，包围形式参数表
调用一个函数
改变表达式的运算次序
强制类型转换
定义带参数的宏
包围sizeof操作符的操作数(如果它是类型名) 比如sizeof(int)|

### 运算符优先级问题
|问题|表达式|实际结果|
|.的优先级高于\* 
->操作符用于解决这个问题| \*p.f|\*(p.f)|
|[]高于\*| int \*ap[]|ap是元素为int指针的数组 int \*(ap[])|
|()高于\*| int \*ap()|ap是函数,返回int \*, int \*(fp())|
|==和!=高于位运算符|(val & mask !=0)|
|==和!=高于赋值符| c=getchar() != EOF| c=(getchar() != EOF)|
|算数运算高于位移运算符|msb << 4 + lsb|msb << (4+lsb)|
|逗号运算符在所有运算符中优先级最低|i=1,2|(i=1),2|
	(i=1,2)表达式中，i=1,但表达式值是2
	或许我可以牢记优先级:乘法、除法优先加法、减法,涉及其他操作符一律加括号

40页小启发
