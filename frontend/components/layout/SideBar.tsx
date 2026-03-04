/**
 * Sidebar.tsx
 *
 * Sidebar navigation for the crypto dashboard.
 *
 * This provides navigation links to the main sections
 * of the application.
 */

"use client"

import Link from "next/link"

export default function Sidebar() {

  return (

    <aside className="w-64 bg-gray-900 text-white h-screen p-6">

      <h2 className="text-2xl font-bold mb-8">
        CryptoTracker
      </h2>

      <nav className="flex flex-col space-y-4">

        <Link
          href="/"
          className="hover:text-blue-400"
        >
          Dashboard
        </Link>

        <Link
          href="/coins"
          className="hover:text-blue-400"
        >
          Coins
        </Link>

        <Link
          href="/portfolio"
          className="hover:text-blue-400"
        >
          Portfolio
        </Link>

      </nav>

    </aside>

  )

}