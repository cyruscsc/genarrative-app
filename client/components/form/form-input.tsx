import React from 'react'
import { UseFormRegisterReturn } from 'react-hook-form'

interface FormInputProps {
  type: 'text' | 'password'
  id: string
  placeholder: string
  error: string | undefined
  register: UseFormRegisterReturn
}

const FormInput = ({ error, register, ...rest }: FormInputProps) => {
  return (
    <input
      {...register}
      {...rest}
      className={`bg-transparent h-9 w-60 px-2 rounded-md appearance-none outline-none selection:bg-storm-400 selection:text-storm-100 duration-200 ${
        error ? 'shadow-[0_0_0_1px_red] focus:shadow-[0_0_0_2px_red]' : 'shadow-storm-300 shadow-[0_0_0_1px] focus:shadow-storm-500 focus:shadow-[0_0_0_2px]'
      }`}
    />
  )
}

export default FormInput
