const API_ROOT = process.env.API_ROOT

/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${API_ROOT}/:path*`,
      },
    ]
  },
}

export default nextConfig
