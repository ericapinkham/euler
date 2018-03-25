import scala.io.Source

object Euler013 extends App {
	val numberSum = Source.fromFile("resources/013.txt").getLines().map(BigInt(_)).sum.toString().substring(0,10)

	println(numberSum)
}
