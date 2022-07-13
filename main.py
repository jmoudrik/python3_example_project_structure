# we see the module here directly
import mylib

from mylib.compute.count import div
from mylib.io.console import println
from mylib import boxed

mylib.println("hi, one line")
boxed("hi, boxed")

boxed(mylib.compute.functional.reduce_add(range(20)))

println(div(10, 5))
println(div(10, 0))
