(defun factorial (n)
  (if (= n 1)
    1
    (* n (factorial (- n 1)))))

(format t "~A" (/  (factorial 40) (* (factorial 20) (factorial 20))))

