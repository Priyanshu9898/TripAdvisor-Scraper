import Image from 'next/image'
import React, { FC } from 'react'

const Loading:FC = () => {
  return (
    <Image src="/loader.gif" width={150} height={150} alt="Loading..." />
  )
}

export default Loading