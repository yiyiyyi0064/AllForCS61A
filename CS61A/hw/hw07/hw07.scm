(define (square n) (* n n))



(define (pow base exp) (cond ((= exp 1) base)

  ((even? exp) (square (pow base (/ exp 2))))

  (else (* base (square (pow base (/ (- exp 1) 2)))) )))



(define (repeatedly-cube n x)

  (if (zero? n)

      x

      (let ((y (repeatedly-cube (- n 1) x)))

      

        (* y y y))))



(define (cddr s) (cdr (cdr s)))


; returns the second element
(define (cadr s) (car (cdr s)))



(define (caddr s) (car (cddr s)))