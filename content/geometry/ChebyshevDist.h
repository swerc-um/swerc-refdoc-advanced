/**
 * Author: Wikipedia
 * Description: Chebyshev distance
 * Given points $(x, y)$ and you need to calculate the Manhattan distances between them, instead of using $|x1-x2|+|y1-y2|$ you can first convert all points $(x, y)$ into $(x+y, x-y)$ and the distances will become $max(|x1-x2|, |y1-y2|)$
 * $(x, y, z)$ to the point $(x + y + z, x + y — z, x — y + z, -x + y + z)$
 * Time: X
 */