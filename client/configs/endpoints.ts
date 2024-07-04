const root = '/api'

const endpoints = {
  user: {
    signIn: {
      method: 'POST',
      path: `${root}/user/sign-in`,
    },
    signUp: {
      method: 'POST',
      path: `${root}/user/sign-up`,
    },
    signOut: {
      method: 'POST',
      path: `${root}/user/sign-out`,
    },
  },
}

export default endpoints
