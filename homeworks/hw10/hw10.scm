(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (define (acc combiner start n term rem)
    (if (= n 0)
      rem
      (acc combiner start (- n 1) term (combiner (term n) rem))
    )
  )
  (acc combiner start n term start)
)

(define-macro (list-of expr for var in seq if filter-fn)
  'YOUR-CODE-HERE
)
