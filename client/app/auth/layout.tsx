import React from 'react'

const AuthLayout = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return (
    <div className='flex min-h-screen min-h-svh flex-col items-center justify-center'>
      <div className='border border-storm-300 rounded-xl p-8'>
      {children}
      </div>
    </div>
  )
}

export default AuthLayout
