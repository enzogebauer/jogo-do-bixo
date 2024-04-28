export function Total({ total }) {

  return (
    <div className=" mt-4 text-white">
      {
        (total > 21) && <h1>Bust!</h1>
      }
      <h1 data-testid="text-2xl">Your hand ({total})</h1>
    </div>
  )
}
