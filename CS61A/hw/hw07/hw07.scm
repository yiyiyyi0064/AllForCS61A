(define (square n) (* n n))

(define (pow base exp) (cond ((= exp 1) base)
  ((even? exp) (square (pow base (/ exp 2))))
  (else (* base (square (pow base (/ (- exp 1) 2)))) )))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
      ;��һֱ��n=0 Ȼ����һ��һ�㷵�ص�n �������һ�ν�� Ȼ�󷵻�
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE)

(define (caddr s) 'YOUR-CODE-HERE)