import React from 'react'

interface FormRootProps {
  onSubmit: React.FormEventHandler<HTMLFormElement>
  children: React.ReactNode
}

const FormRoot = ({ onSubmit, children }: FormRootProps) => {
  return (
    <form onSubmit={onSubmit} className='flex flex-col gap-4'>
      {children}
    </form>
  )
}

export default FormRoot
