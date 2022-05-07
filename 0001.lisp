(defun main () 
  (let ((muls (loop as x from 0 upto 999 collect (if (or (= 0 (mod x 3)) (= 0 (mod x 5))) x))))
    (apply '+ (remove nil muls))))

(format t "~A" (main))
     
