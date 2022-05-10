(define (sum-of-divisors n)
  (define (go num sum)
    (if (> num (sqrt n))
      sum
      (if (= 0 (modulo n num))
        (go (+ 1 num) (+ sum num (/ n num)))
        (go (+ 1 num) sum))))
  ;; num taken as 2 coz 0 doesnt make sense 
  ;; and 1 will include the original number in the sum 
  ;; which is not supposed to happen
  ;;
  ;; sum taken as 1 because num 1 was skipped 
  ;; and we have to consider 1 as a proper divisor
  (go 2 1))

(define (abundant? n)
  (if (< n (sum-of-divisors n))
    #t
    #f))

(define (print-all-abundant)
  (define (go n)
    ;; all integers greater than 28123 can be written 
    ;; as the sum of two abundant numbers
    (if (>= n 28123)
      #t
      (begin
        (if (abundant? n) (format #t "~A\n" n))
        (go (+ 1 n)))))
  (go 0))

(define (main))
