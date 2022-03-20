? = 1 or 0 character
. = any character
+ = 1 or more
hahaha* = 0 or more
{m, n} = max > ... > min [abc] = match a or b or c
(t|T) = match t or T
^start = match start
end$ = match end
(?<=[T|t]he). = search behind and not include in result
(?<![T|t]he). = search behind and not contain "The" or "the" behind
.(?at) = search after and contain "at"
(?<namegroup>\d{3}) = named for group, select group by $namegroup
(?:) = not capturing group

REFERENCE: https://www.youtube.com/watch?v=rhzKDrUiJVk