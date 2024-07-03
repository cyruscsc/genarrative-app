import React from 'react'

const FormField = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return <div className='flex flex-col space-y-1'>{children}</div>
}

export default FormField
