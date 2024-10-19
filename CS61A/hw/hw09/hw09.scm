(define (curry-cook formals body) 
          (if (null? formals) ;先思考结束条件 最搞笑的是语法和python搞混了
            body  ;如果这个时候formals已经生成完了 那就直接打印body就ok
            (cons `(lambda (,(car formals))) ,(curry-cook (cdr formals) body)))
            ;,(car formals) 只formals car就不会解析
            ;这个recursive有进步但不多 
)

(define (curry-consume curry args) 
          if( (null? (cdr args))
          ; (1) 只剩一个参数了 就不再迭代 直接返回它的值就可以 其他已经存在lambda中 最后会直接计算
            (curry (car args))
            (curry-consume (curry (car args)) (cdr args)))
          
          
  )

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons '(cond)
        (map (lambda (option) ;是传入的所有options中的car
               (cons  '(equal? ,(car (cdr switch-expr)) ,(cdr option) ) (cdr option)))
             (car (cdr (cdr switch-expr))))))

 (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))
