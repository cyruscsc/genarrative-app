import React from 'react'

interface FormButtonProps {
  label: string
}

const FormButton = ({ label }: FormButtonProps) => {
  return (
    <button
      type='submit'
      className='bg-sand-500 rounded-md border border-sand-700 py-2 px-4 mt-2 text-base hover:brightness-110 duration-200'
    >
      {label}
    </button>
  )
}

export default FormButton
