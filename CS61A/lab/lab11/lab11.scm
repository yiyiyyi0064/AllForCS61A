(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false))
  

(define (square n) (* n n))

(define (pow-expr base exp) 
(cond ((= exp 0) 1)
  ((= exp 1) `(* ,base ,exp))
  ((even?  exp )  
  (cons `square  (list(pow-expr base (/ exp 2))))
  ;construct the square
  )
  (else
  ;还是得加list 来加括号 不然cons就会把前后直接拼在一起
  (cons '* (cons base (list(cons 'square  (list(pow-expr base (/ (- exp 1) 2))) ))))
  )
  ))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))
  ;这里不再需要` 因为macro会自动作为data 不去evaluate

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin (f) (repeated-call (- n 1) f))))
