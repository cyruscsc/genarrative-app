import { AuthForm } from '@/components'
import { CardBody, CardFoot, CardHead, CardRoot } from '@/components/card'
import { routes } from '@/configs'
import Link from 'next/link'

const SignIn = () => {
  return (
    <CardRoot>
      <CardHead
        title={routes.signIn.title}
        description={routes.signIn.description}
      />
      <CardBody>
        <AuthForm type='sign-in' />
      </CardBody>
      <CardFoot>
        <p>
          Don't have an account?{' '}
          <Link href={routes.signUp.path} className='underline'>
            {routes.signUp.title}
          </Link>
        </p>
      </CardFoot>
    </CardRoot>
  )
}

export default SignIn
