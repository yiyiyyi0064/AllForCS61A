(define (ascending? s) (cond 
((null? s) #t)                      
((null? (cdr s)) #t)  
((> (car s) (car (cdr s))) #f)
(else (ascending? (cdr s) ) )
                                )
    )

    

    



(define (my-filter pred s) (cond ((null? s) '())
                                 ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    (else (my-filter pred (cdr s)))))




(define (interleave lst1 lst2) (cond ((null? lst1) lst2)
                                    ((null? lst2) lst1)
    (else (cons (car lst1) (interleave lst2 (cdr lst1))))
    ))



(define (no-repeats s) (cond(       ((null? s) '())
                                    (else  (cons (car s) (filter (lambda (x) (not (= (car s) x))) (cdr s)) )) ;生成新的s 同时进入recursive
                                    ; 我之前一直想的是 直接得到filter的s 然后最后返回 但是我没有考虑到recursive的特性 其实重新构造一个list会更加好
                                    ))
                                    )

