(define fact (lambda (n)
  (if (zero? n) 1 (* n (fact(- n 1))))))
  ;define a function fact

(fact 5)
;120

(define-macro (trace expr) ;(trace (fact 5))
  (define operator (car expr)) ;fact get the name of the function to print the name
  `(begin ;begin 以此执行expr1到exprN 并返回最后一个表达式的值
        (define original ,operator) ;所有都quasi了 要让original得到function name to call
        (define ,operator (lambda (n)
        ;这里其实是改变了operator bound to 但是没有改变name 下面调用的时候还没改变
                              (print (list (quote ,operator) n)) ;print a list (content)                    
                              ; 当没有quote时 会打印 procudure of the function and I dont need the procudure 
                              ; 因为返回之后是会找到这个name表示什么 所以必须quote一下保持其原名
                              (original n))) ;call the original function and excecute it))
        (define result ,expr) ;excecute the original expression 我们在做的其实是在分解那个表达 其实可以直接计算
        (define ,operator original) ;change the operator to the original
        ;所以最后返回调用的时候operator其实是这个
        result ;return the final result
        )
)

(trace (fact 5))

(fact 5)