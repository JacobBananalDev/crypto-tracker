/**
 * coins/[symbol]/page.tsx
 *
 * Dynamic page used for displaying a single cryptocurrency.
 *
 * Example routes:
 * /coins/BTC
 * /coins/SOL
 * /coins/XRP
 *
 * This page loads chart data from the backend
 * and renders a price chart.
 */

"use client"

import { useEffect, useState, use } from "react"
import { getCoinChart } from "@/lib/api"
import PriceChart from "@/components/charts/PriceChart"

interface ChartPoint {
  time: string
  price: number
}

export default function CoinPage({
  params
}: {
  params: Promise<{ symbol: string }>
}) {

  // unwrap async params
  const { symbol } = use(params)

  const coinSymbol = symbol.toUpperCase()

  const [chartData, setChartData] = useState<ChartPoint[]>([])
  const [loading, setLoading] = useState(true)

  /**
   * Fetch chart data for the selected coin
   */
  useEffect(() => {

    async function fetchChart() {

      try {

        const data = await getCoinChart(coinSymbol)

        setChartData(data)

      }
      catch (error) {

        console.error("Failed to load chart", error)

      }
      finally {

        setLoading(false)

      }

    }

    fetchChart()

  }, [coinSymbol])

  if (loading) {
    return <div>Loading chart...</div>
  }

  return (

    <div>

      <h1 className="text-3xl font-bold mb-6">
        {coinSymbol} Price Chart
      </h1>

      <PriceChart
        title={`${coinSymbol} Price History`}
        data={chartData}
      />

    </div>

  )

}