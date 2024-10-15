(define (over-or-under num1 num2) (cond ((< num1 num2) -1)
                                        ((> num1 num2) 1)
                                        ((= num1 num2) 0))
                                        )

(define (make-adder num) (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n) 
  (lambda (x) (if (> (- n 1) 0)
  ((repeat f (- n 1))(f x))
  (f x))
        )
  )

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) (cond ((= (modulo a b) 0) b)
  ((= (modulo b a) 0) a)
  ((> a b) (gcd b (modulo a b)))
  ((< a b)  (gcd a (modulo b a)))))
