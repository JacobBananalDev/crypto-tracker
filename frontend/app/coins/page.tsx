/**
 * coins/page.tsx
 *
 * Displays all tracked cryptocurrencies stored in the backend.
 *
 * This page fetches coins from the FastAPI API and renders
 * them in a simple table-style layout.
 */

"use client"

import { useEffect, useState } from "react"
import { getCoins } from "@/lib/api"
import Image from "next/image"

interface Coin {
  id: number
  symbol: string
  name: string
  image_url: string
}

export default function CoinsPage() {

  const [coins, setCoins] = useState<Coin[]>([])
  const [loading, setLoading] = useState(true)

  /**
   * Fetch coin list from backend when page loads
   */
  useEffect(() => {

    async function fetchCoins() {

      try {

        const data = await getCoins()

        setCoins(data)

      }
      catch (error) {

        console.error("Failed to load coins", error)

      }
      finally {

        setLoading(false)

      }

    }

    fetchCoins()

  }, [])

  if (loading) {

    return (
      <div className="text-lg">
        Loading coins...
      </div>
    )

  }

  return (

    <div>

      <h1 className="text-3xl font-bold mb-6">
        Coins
      </h1>

      <div className="bg-white shadow rounded-xl">

        {coins.map((coin) => (

          <div
            key={coin.id}
            className="flex items-center justify-between p-4 border-b"
          >

            <div className="flex items-center gap-4">

              <img
                src={coin.image_url}
                alt={coin.symbol}
                className="w-8 h-8"
              />

              <div>

                <div className="font-semibold">
                  {coin.symbol}
                </div>

                <div className="text-gray-500 text-sm">
                  {coin.name}
                </div>

              </div>

            </div>

          </div>

        ))}

      </div>

    </div>

  )

}