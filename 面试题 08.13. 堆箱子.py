class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        @functools.lru_cache(maxsize=3000)
        def sol(w, d, h) :
            inners = [(iw,id,ih) for iw,id,ih in box if iw<w and id<d and ih<h]
            if not inners : return h
            return max((sol(iw,id,ih) for iw,id,ih in inners)) + h
        return max((sol(w,d,h) for w,d,h in box))
    