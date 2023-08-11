import Image from 'next/image'
import React, { FC } from 'react'

const Loading:FC = () => {
  return (
    <Image src="/loader.gif" width={200} height={200} alt="Loading..." />
  )
}

export default Loading