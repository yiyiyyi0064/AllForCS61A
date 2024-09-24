**Iterator**

**Def**: An **iterable** is an object on which calling the built-in `iter` function returns an *iterator*. An **iterator** is an object on which calling the built-in `next` function returns the next value.

![image-20240920092303740](C:\Users\yiyiyyi\AppData\Roaming\Typora\typora-user-images\image-20240920092303740.png)

**t is an object, not a list.**

But it can be used in a for statement bc all iterators are iterable.

> What is **iterable**?
>
> 1、它是能够一次返回一个成员的对象，也就是可以 for…in 遍历的；
>
> 2、所有的序列类型（也就是后面要说到的 Sequence），都是可迭代对象，如 list、str、tuple，还有映射类型 dict、文件对象等非序列类型也是可迭代对象；
>
> 3、自定义对象在实现了 **iter**() 方法或者实现了 **getitem**() 方法后，也可以成为可迭代对象；
>
> 4、**iter()**方法接受一个可迭代对象，该方法的返回值是一个迭代器（Iterator）

---

##### Discussion 5 Tree

Review key functions with max

max(s,key=f) returns the item x in s for which f(x) is largest. **caution: return x instead of f(x)!!!**

---

Lab 05 

感觉tree这里重点要学

recursive的思想特别重要呀

---

Generator

![image-20240920205223093](C:\Users\yiyiyyi\AppData\Roaming\Typora\typora-user-images\image-20240920205223093.png)