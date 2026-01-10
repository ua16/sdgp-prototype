<script lang="ts">
    let { quotedata } = $props();
    let currencyFormatter = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
    });
</script>

<div
    class="flex flex-col bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">Cargo Information</div>

    <div class="flex flex-row w-full items-center mt-5 mb-3">
        <div class="flex flex-col w-1/3">
            <div class="text-sm text-stone-800">Cargo Type</div>
            <div class="text-lg font-bold">{quotedata.cargoType}</div>
        </div>
        <div class="flex flex-col w-1/3 items-center">
            <div class="text-sm text-stone-800">Commodity</div>
            <div class="text-lg font-bold">{quotedata.commodity}</div>
        </div>
        <div class="flex flex-col w-1/3 items-end">
            <div class="text-sm text-stone-800"># HS Code</div>
            <div class="text-lg font-bold">{quotedata.hsCode}</div>
        </div>
    </div>

    <hr class="border-stone-300" />

    <div class="flex flex-row w-full items-center mt-5 mb-3">
        <div class="flex flex-col w-1/3">
            <div class="text-sm text-stone-800">Net Weight</div>
            <div class="text-lg font-bold">{quotedata.netWeight} kg</div>
        </div>
        <div class="flex flex-col w-1/3 items-center">
            <div class="text-sm text-stone-800">Height</div>
            <div class="text-lg font-bold">{quotedata.height} cm</div>
        </div>
        <div class="flex flex-col w-1/3 items-end">
            <div class="text-sm text-stone-800">Width</div>
            <div class="text-lg font-bold">{quotedata.width} cm</div>
        </div>
    </div>

    <hr class="border-stone-300" />

    <div class="flex flex-col w-1/3 mt-5">
        <div class="text-sm text-stone-800">Declared Value</div>
        <div class="text-lg font-bold">
            {currencyFormatter.format(quotedata.cargoValue)}
        </div>
    </div>
</div>
