(define fact (lambda (n)
  (if (zero? n) 1 (* n fact(- n 1)))))

(fact 5)

(define-macro (trace expr) ;(trace (fact 5))
  (define operator (car expr)) ;fact
  `(begin
        (define original ,operator) ;the fact function
        (define ,operator (lambda (n)
                              (print (list (quote ,operator) n)) ;print a list (content)                    
                              (original n))) ;call the original function and excecute it))
        (define result ,expr) ;excecute the original expression
        (define ,operator original) ;change the operator to the original
        result ;return the final result
        )
)

(trace (fact 5))

(fact 5)