import { toAddress, toBigNumber } from "@rarible/types"
import { SellRequest } from "@rarible/protocol-ethereum-sdk/build/order/sell"
import React, { useState } from "react"
import { NftItem } from "@rarible/protocol-api-client"
import { SimpleOrder } from "@rarible/protocol-ethereum-sdk/build/order/sign-order"
import { RaribleSdk } from "@rarible/protocol-ethereum-sdk"
import URLPatch from './URLPatch'

type CreateOrderFormState = {
	contract: string,
	tokenId: string,
	price: string,
	hash: string
}

type BuyOrderFormState = {
	hash: string,
	amount: string
}

type DashboardProps = {
	provider: any
	sdk: RaribleSdk
	accounts: string[]
}

const Dashboard: React.FC<DashboardProps> = ({ provider, sdk, accounts }) => {
	const [ownedItems, setOwnedItems] = useState<NftItem[]>()
	const [order, setOrder] = useState<SimpleOrder>()
	const [createOrderForm, setCreateOrderForm] = useState<CreateOrderFormState>({
		contract: '',
		tokenId: '',
		price: '10',
		hash: '',
	})
	const [purchaseOrderForm, setPurchaseOrderForm] = useState<BuyOrderFormState>({ hash: '', amount: '1' })
	/**
	 * Handle connect to wallet
	 */
	const connectWalletHandler = () => {
		provider.request({ method: 'eth_requestAccounts' })
		// URLPatch.init() // CHANGE ON BROWSER : EXAMPLE => http://localhost:3000/?OrderHash=0xdfa3eed367ebf346a1469100df138cf8ec4d0b07b1ea7acd18ddd4752e9e6e28&Amount=1&contract=0x6ede7f3c26975aad32a475e1021d8f6f39c89d82&tokenId=102269783871445009689193659504668254296443359178228636083094963402840245237813&price=10
	}

	const URLPatcher = () => {
		// URLPatch.init() // CHANGE ON BROWSER : EXAMPLE => http://localhost:3000/?OrderHash=0xdfa3eed367ebf346a1469100df138cf8ec4d0b07b1ea7acd18ddd4752e9e6e28&Amount=1&contract=0x6ede7f3c26975aad32a475e1021d8f6f39c89d82&tokenId=102269783871445009689193659504668254296443359178228636083094963402840245237813&price=10
		connectWalletHandler()
	}


	/**
	 * Mint Nft
	 */
	const lazyMint = async () => {
		const item = await sdk.nft.mintLazy({
			'@type': 'ERC721',
			contract: toAddress('0x6ede7f3c26975aad32a475e1021d8f6f39c89d82'), // rinkeby default Rarible collection
			uri: "/ipfs/QmWLsBu6nS4ovaHbGAXprD1qEssJu4r5taQfB74sCG51tp",
			creators: [{ account: toAddress(accounts[0]), value: 10000 }],
			royalties: [],
		})
		if (item) {
			/**
			 * Get minted nft through SDK
			 */
			const token = await sdk.apis.nftItem.getNftItemById({ itemId: item.id })
			if (token) {
				setCreateOrderForm({
					...createOrderForm,
					contract: token.contract,
					tokenId: token.tokenId,
				})
			}
		}
	}

	/**
	 * Create sell order from minted nft
	 */
	function sactionOrder() {
		// createOrderForm.contract = '0x6ede7f3c26975aad32a475e1021d8f6f39c89d82'
		// createOrderForm.tokenId = '102269783871445009689193659504668254296443359178228635795104556773702935654691'
		// createOrderForm.price = '10'
		var contract = '0x00';
		var tokenId = '0x00';
		var price = '1';
		var contractFetcher = new URL(window.location.href).searchParams.get('contract')
		if (contractFetcher!=null) {contract = contractFetcher}
		var tokenIdFetcher = new URL(window.location.href).searchParams.get('tokenId')
		if (tokenIdFetcher!=null) {tokenId = tokenIdFetcher}
		var priceFetcher = new URL(window.location.href).searchParams.get('price')
		if (priceFetcher!=null) {price = priceFetcher}
		createOrderForm.contract = contract
		createOrderForm.tokenId = tokenId
		createOrderForm.price = price

		createSellOrder()
	}

	const createSellOrder = async () => {
		if (createOrderForm.contract && createOrderForm.tokenId && createOrderForm.price) {
			const request: SellRequest = {
				makeAssetType: {
					assetClass: "ERC721",
					contract: toAddress(createOrderForm.contract),
					tokenId: toBigNumber(createOrderForm.tokenId),
				},
				amount: 1,
				maker: toAddress(accounts[0]),
				originFees: [],
				payouts: [],
				price: toBigNumber(createOrderForm.price),
				takeAssetType: { assetClass: "ETH" },
			}
			// Create an order
			const resultOrder = await sdk.order.sell(request).then(a => a.runAll())
			if (resultOrder) {
				setOrder(resultOrder)
				setPurchaseOrderForm({ ...purchaseOrderForm, hash: resultOrder.hash })
			}
		}
	}

	/**
	 * Buy order
	 */
	const handlePurchaseOrder = async () => {
		// createSellOrder()
		URLPatch.sactionURLPatcher()
		if (order) {
			await sdk.order.fill(order, { amount: parseInt(purchaseOrderForm.amount) }).then(a => a.runAll())
		}
	}

	/**
	 * Handle get NFT's owned by connected wallet
	 */
	const handleGetMyNfts = async () => {
		const items = await sdk.apis.nftItem.getNftItemsByOwner({ owner: accounts[0] })
		setOwnedItems(items?.items)
	}

	/**
	 * input handlers
	 */
	const handleChangeOrderContract = (e: React.FormEvent<HTMLInputElement>): void => {
		setCreateOrderForm({ ...createOrderForm, contract: e.currentTarget.value })
	}
	const handleChangeOrderTokenId = (e: React.FormEvent<HTMLInputElement>): void => {
		setCreateOrderForm({ ...createOrderForm, tokenId: e.currentTarget.value })
	}
	const handleChangeOrderPrice = (e: React.FormEvent<HTMLInputElement>): void => {
		setCreateOrderForm({ ...createOrderForm, price: e.currentTarget.value })
	}
	const handleOrderHash = (e: React.FormEvent<HTMLInputElement>): void => {
		setPurchaseOrderForm({ ...purchaseOrderForm, hash: e.currentTarget.value })
	}
	const handlePurchaseOrderAmount = (e: React.FormEvent<HTMLInputElement>): void => {
		setPurchaseOrderForm({ ...createOrderForm, amount: e.currentTarget.value })
	}
	return (
		<div className="App">
			<video width="100%" height="100%" autoPlay loop playsInline>
				<source src="https://www.dropbox.com/s/1c4q3xsw409euis/background-compressed.mp4?raw=1" type="video/mp4"></source>
			</video>
			<div className='subClass'>
				<button onClick={URLPatcher} disabled={!!provider?.selectedAddress}>
					{accounts.length ? 'Connected' : 'Connect wallet'}
				</button>
				<div>{accounts.length && <span>{accounts[0]}</span>}</div>
				<div style={{ padding: '4px' }} className='NN'>
					<p>Mint item form (TODO)</p>
					<button onClick={lazyMint}>lazy mint</button>
				</div>
			</div>

			<div style={{ padding: '4px' }} className='NN'>
				<p>Create sell order form</p>
				<div><input onChange={handleChangeOrderContract} value={createOrderForm?.contract} placeholder={"Contract address"} /></div>
				<div><input onChange={handleChangeOrderTokenId} value={createOrderForm?.tokenId} placeholder={"Token Id"} /></div>
				<div><input onChange={handleChangeOrderPrice} value={createOrderForm?.price} placeholder={"Price"} /></div>
				<button onClick={createSellOrder}>
					Sell
				</button>
			</div>

			<div /* style={{ padding: '4px' }} */ >
				<p>Create Buy Order and Purchase NFT</p>
				<div><button onClick={sactionOrder}>Sanction Buy Order</button></div>
				<div><input onChange={handleOrderHash} value={purchaseOrderForm.hash} placeholder={'Order hash'} name="OrderHash" id="OrderHash" onClick={URLPatcher} /></div>
				<div><input onChange={handlePurchaseOrderAmount} value={purchaseOrderForm.amount} placeholder={'Amount'} id="Amount" onClick={URLPatcher} /></div>
				<div><button onClick={handlePurchaseOrder}>Purchase</button></div>
			</div>

			<div className='NN'>
				<p>NFT items owned by me: <button onClick={handleGetMyNfts}>Refresh</button></p>
				<ul>
					{ownedItems?.length && ownedItems.map(i => {
						return (
							<li key={i.id}>
								<p><strong>Item</strong> id: {i.id}</p>
								<p><strong>Lazy supply:</strong> {i.lazySupply}</p>
							</li>
						)
					})}
				</ul>
			</div>
		</div>
	)
}

export default Dashboard
