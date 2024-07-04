import React from 'react'

const CardRoot = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return (
    <article className='flex flex-col justify-center gap-4 border border-storm-300 rounded-xl p-8'>
      {children}
    </article>
  )
}

export default CardRoot
