import React from 'react'

const CardBody = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return (
    <div>{children}</div>
  )
}

export default CardBody