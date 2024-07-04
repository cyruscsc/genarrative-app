interface CardHeadProps {
  title: string
  description?: string
}

const CardHead = ({ title, description }: CardHeadProps) => {
  return (
    <div className='flex flex-col gap-1 justify-center'>
      <h2 className='font-medium text-2xl'>{title}</h2>
      {description && <p className='font-light text-xs'>{description}</p>}
    </div>
  )
}

export default CardHead
