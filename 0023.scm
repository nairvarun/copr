(define (sum-of-divisors n)
  (define (go num sum)
    (if (>= num (sqrt n))
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

(define (get-abundant-till n)
  (define (go inner-num all-nums)
    (if (> inner-num n)
      (filter abundant? all-nums)
      (go (+ 1 inner-num)
          (append all-nums (list inner-num)))))
  (go 1 '()))

