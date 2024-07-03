'use client'

import * as Label from '@radix-ui/react-label'
import { SubmitHandler, useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { FormButton, FormField, FormInput, FormMessage, FormRoot } from './form'

interface AuthFormProps {
  type: 'sign-in' | 'sign-up'
}

const AuthForm = ({ type }: AuthFormProps) => {
  const schema =
    type === 'sign-in'
      ? z.object({
          email: z.string().email({ message: 'Invalid email address' }),
          password: z.string(),
        })
      : z.object({
          email: z.string().email({ message: 'Invalid email address' }),
          password: z.string().min(6, { message: 'At least 6 characters' }),
        })

  type Schema = z.infer<typeof schema>

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Schema>({ resolver: zodResolver(schema) })

  const submitForm: SubmitHandler<Schema> = (data) => console.log(data)

  return (
    <FormRoot onSubmit={handleSubmit(submitForm)}>
      <FormField>
        <Label.Root htmlFor='email'>Email</Label.Root>
        <FormInput
          type='text'
          id='email'
          placeholder='you@example.com'
          error={errors.email?.message}
          register={register('email')}
        />
        <FormMessage message={errors.email?.message} />
      </FormField>
      <FormField>
        <Label.Root htmlFor='password'>Password</Label.Root>
        <FormInput
          type='password'
          id='password'
          placeholder='••••••••'
          error={errors.password?.message}
          register={register('password')}
        />
        <FormMessage message={errors.password?.message} />
      </FormField>
      <FormButton label='Sign In' />
    </FormRoot>
  )
}

export default AuthForm
