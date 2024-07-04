import React from 'react'

const AuthLayout = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return (
    <div className='flex min-h-screen min-h-svh flex-col items-center justify-center'>
      {children}
    </div>
  )
}

export default AuthLayout
