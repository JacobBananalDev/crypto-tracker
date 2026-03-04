/**
 * page.tsx
 *
 * Main dashboard page for the crypto tracker frontend.
 *
 * This page fetches portfolio value data from the FastAPI backend
 * and displays the user's total portfolio value along with each
 * asset's contribution.
 */

"use client"

import { useEffect, useState } from "react"
import { getPortfolioValue } from "@/lib/api"

interface Asset {
  symbol: string
  amount: number
  price_usd: number
  value_usd: number
}

interface PortfolioResponse {
  total_value_usd: number
  assets: Asset[]
}

export default function HomePage() {

  const [portfolio, setPortfolio] = useState<PortfolioResponse | null>(null)
  const [loading, setLoading] = useState(true)

  /**
   * Fetch portfolio value when the page loads.
   */
  useEffect(() => {

    async function fetchPortfolio() {

      try {
        const data = await getPortfolioValue()
        setPortfolio(data)
      }
      catch (error) {
        console.error("Failed to load portfolio", error)
      }
      finally {
        setLoading(false)
      }

    }

    fetchPortfolio()

  }, [])

  if (loading) {
    return (
      <div className="p-10 text-lg">
        Loading portfolio...
      </div>
    )
  }

  return (
    <main className="p-10">

      <h1 className="text-3xl font-bold mb-6">
        Crypto Portfolio Dashboard
      </h1>

      {portfolio && (

        <div className="bg-gray-900 text-white p-6 rounded-xl shadow-lg">

          <h2 className="text-xl mb-2">
            Total Portfolio Value
          </h2>

          <p className="text-4xl font-bold mb-6">
            ${portfolio.total_value_usd.toFixed(2)}
          </p>

          <div className="space-y-2">

            {portfolio.assets.map(asset => (

              <div
                key={asset.symbol}
                className="flex justify-between border-b border-gray-700 pb-2"
              >

                <span>{asset.symbol}</span>

                <span>
                  {asset.amount}
                </span>

                <span>
                  ${asset.value_usd.toFixed(2)}
                </span>

              </div>

            ))}

          </div>

        </div>

      )}

    </main>
  )

}