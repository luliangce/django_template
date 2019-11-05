# DjangoRestful模板

## 这是什么?

这是我在编写基于Django的前后端分离项目时的通用小工具，这些工具致力于约束同一个项目内部的开发者开发不同接口时的行为。

## Why not DRF?

DRF很好，但是相比于引入一个复杂的框架，有时候需要的仅仅是一些微小的patch就能够完成需求。  

## Concept

尽量不修改框架的使用方式，比如默认情况下Django的认证中间件会挂在一个User对象到到request对象上，直接request.user就能读取到。为了保留这个功能，将通过header传递的jwt解析出来之后，也挂在到request上。*未采用Django本身一样的lazy_object逻辑是基于我方本身的业务特点*  
减少重复劳动，类似`json.loads`,构建`HttpResponse`的操作封装成统一的结构，将error code看做类来对待，最大程度的统一非业务逻辑。

## 做了什么? 

代码量很小，就不一一解释了。