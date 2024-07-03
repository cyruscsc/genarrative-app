interface FormMessageProps {
  message: string | undefined
}

const FormMessage = ({ message }: FormMessageProps) => {
  return message && <span className="text-sm text-red-500">{message}</span>
}

export default FormMessage
