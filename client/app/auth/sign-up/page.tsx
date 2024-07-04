import { AuthForm } from '@/components'
import { CardBody, CardFoot, CardHead, CardRoot } from '@/components/card'
import { routes } from '@/configs'
import Link from 'next/link'

const SignUp = () => {
  return (
    <CardRoot>
      <CardHead
        title={routes.signUp.title}
        description={routes.signUp.description}
      />
      <CardBody>
        <AuthForm type='sign-up' />
      </CardBody>
      <CardFoot>
        <p>
          Have an account?{' '}
          <Link href={routes.signIn.path} className='underline'>
            {routes.signIn.title}
          </Link>
        </p>
      </CardFoot>
    </CardRoot>
  )
}

export default SignUp
